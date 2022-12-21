from useGrobid import useGrobid
from XMLtoTXT import XMLtoTXT
from useModelHuggingface import useModel
from addRegex import addRegex
from calcF1Score import calcF1Score

import sys, getopt, argparse


def main(argv):

    parser = argparse.ArgumentParser(
        description="Deteccion de agradecimientos en proyectos software"
    )
    parser.add_argument("-a", "--articulos", type=str, help="Carpeta de los articulos")
    parser.add_argument(
        "-t", "--tei", type=str, help="Carpeta para guardar los XML y TXT"
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Carpeta para guardar los json devueltos"
    )
    parser.add_argument("-m", "--model", type=str, help="Modelo de HuggingFace")
    parser.add_argument(
        "-s", "--goldstandard", type=str, help="Carpeta donde esta el goldstandard"
    )
    parser.add_argument(
        "-g",
        "--grobid",
        action="store_true",
        help="Usar grobid para pasar articulos de PDF a XML",
    )
    parser.add_argument(
        "-x",
        "--toTXT",
        action="store_true",
        help="Sacar la seccion de Acknowledgements en TXT",
    )
    parser.add_argument(
        "-f", "--huggingface", action="store_true", help="Usar modelo de HuggingFace"
    )
    parser.add_argument(
        "-r",
        "--regex",
        action="store_true",
        help="Mete al json del modelo lo encontrado con regex",
    )
    parser.add_argument(
        "-c", "--calcF1", action="store_true", help="Calcula el F1 score en una tabla"
    )

    args = parser.parse_args()

    articulos = ""
    TEIfolder = ""
    output = ""
    model = ""
    goldstandard = ""
    opts, args = getopt.getopt(
        argv,
        "ha:t:o:m:s:gxfrc",
        [
            "articulos=",
            "TEIfolder=",
            "ofile=",
            "model=",
            "goldstandard=",
            "grobid=",
            "toTXT=",
            "huggingface=",
            "regex=",
            "calcF1=",
        ],
    )
    for opt, arg in opts:
        if opt == "-h":
            print(
                "main.py -a <articulos> -t <tei> -o <output> -m <modelname> -s <goldstandard> -g -x -f -r -c"
            )
            sys.exit()
        elif opt in ("-a", "--articulos"):
            articulos = arg
        elif opt in ("-t", "--tei"):
            TEIfolder = arg
        elif opt in ("-o", "--ofile"):
            output = arg
        elif opt in ("-m", "--model"):
            model = arg
        elif opt in ("-s", "--goldstandard"):
            goldstandard = arg
        elif opt in ("-g", "--grobid"):
            useGrobid(articulos, TEIfolder)
        elif opt in ("-x", "--toTXT"):
            XMLtoTXT(TEIfolder)
        elif opt in ("-f", "--huggingface"):
            useModel(model, TEIfolder + "TXT/", output)
        elif opt in ("-r", "--regex"):
            addRegex(model, TEIfolder + "TXT/", output)
        elif opt in ("-c", "--calcF1"):
            calcF1Score(output + model + "/", goldstandard)


if __name__ == "__main__":
    main(sys.argv[1:])
