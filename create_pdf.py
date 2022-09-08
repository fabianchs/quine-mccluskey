import numpy as np
import os, glob
from pylatex import Document, Section, Subsection, Tabular, Command
from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
from main import exp_output_pdf, iter_output_pdf
from pylatex import PageStyle, Head, Foot, MiniPage, \
    StandAloneGraphic, MultiColumn, Tabu, LongTabu, LargeText, MediumText, \
    LineBreak, NewPage, Tabularx, TextColor, simple_page_number, Itemize, Hyperref, Package
from pylatex.utils import italic, bold, NoEscape, escape_latex
import os
import pandas as pd


def hyperlink(url,text):
    text = escape_latex(text)
    return NoEscape(r'\href{' + url + '}{' + text + '}')

event_info_dir = 'events_station_info'
all_station_info_files = glob.glob(f"{event_info_dir}/*.txt")
event_maps_dir = 'events_station_maps'

iteration=0




if __name__ == '__main__':

    geometry_options = {"tmargin": "1cm", "lmargin": "1cm", "margin": "1cm"}
    doc = Document(geometry_options=geometry_options, 
            documentclass="beamer",
            )
    doc.packages.append(Package('hyperref'))
    
    with doc.create(Section('Titlepage')):
        doc.preamble.append(Command('title', 'Algoritmo Quine McCluskey'))
        doc.preamble.append(Command('author', 'Fabián Chacón, Johanel Álvarez, William Sánchez'))
        doc.preamble.append(Command('date', "8 setiembre 2022"))
        doc.append(NoEscape(r'\maketitle'))

    with doc.create(Section('Section')):
        with doc.create(Itemize()) as itemize:
            for i in range(0,len(iter_output_pdf)-1,2):
                iteration+=1
                itemize.add_item("ITERACIÓN: "+str(iteration))
                for j in iter_output_pdf[i]:
                    itemize.add_item("Cantidad de 1: "+str(j))
                    for k in iter_output_pdf[i][j]:  

                        if iteration>=3:
                            itemize.add_item(k[1])
                        elif i>1:
                            itemize.add_item(k[1][1:len(k[1])])
                        else:
                            itemize.add_item(k[1:len(k)])

                doc.append(NewPage())

                itemize.add_item("RELACIONES CON OTRAS EXPRESIONES")
                for l in iter_output_pdf[i+1]:
                    if iteration==1:
                        itemize.add_item([l[0],l[1][1:len(l[1])]])
                    else:
                        itemize.add_item(l)

                doc.append(NewPage())



    with doc.create(Section('Slide')):
        with doc.create(Itemize()) as itemize:
            itemize.add_item("La expresión final es:")
            itemize.add_item(exp_output_pdf)

    totstationslist = []
    for ff in glob.glob(f"{event_maps_dir}/*.png"):
        numstation = int(os.path.basename(ff).split('.png')[0].split("_")[-1])
        totstationslist.append(numstation)
    totstationsinds = np.argsort(totstationslist)
    totstationsinds = totstationsinds[::-1] #reverse order

    for ind in totstationsinds:
        ff = all_station_info_files[ind]
        dff_events = pd.read_csv(ff, nrows=1)
        evname = dff_events.loc[0,'eventorig']
        eventbrk = dff_events.loc[0,'eventbrk']
        # print(evname)
        station_map_file_list = glob.glob(f"{event_maps_dir}/*{evname}_*.png")
        if len(station_map_file_list):
            station_map_file = station_map_file_list[0]
            print(station_map_file)
            with doc.create(Section('Slide')):
                with doc.create(Itemize()) as itemize:
                    itemize.add_item(f"{evname}, Dep: {dff_events.loc[0,'eventdepth']}, Mag: {dff_events.loc[0,'eventmag']}")
                with doc.create(Subsection('Figure')):
                    with doc.create(Figure(position='h!')) as fig_map:
                        fig_map.add_image(station_map_file, width='230px')
                        fig_map.add_caption(f'Station Map for {evname}')

                doc.append(NewPage())

	# Creating a pdf
    doc.generate_pdf('solucion', clean_tex=False, clean=True)

