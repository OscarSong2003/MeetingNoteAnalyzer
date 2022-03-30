from forte import Pipeline
from forte.data.readers import  PlainTextReader
from fortex.spacy import SpacyProcessor

import os
from forte.processors.stave import StaveProcessor
from forte.data.data_pack import DataPack
from forte.pipeline import Pipeline
from forte.utils import utils
from ft.onto.base_ontology import (
    Token,
    Sentence,
    Document,
)
from forte.data.ontology import Annotation
from forte.data.readers import OntonotesReader, AudioReader
from forte.data.data_pack import DataPack
from forte.pipeline import Pipeline

def nameEntityRecognition(path): 
    # notebook should be running from project root folder
    data_path = path;

    # pipeline: Pipeline = Pipeline()
    # pipeline.set_reader(OntonotesReader())
    # pipeline.initialize()
    # data_pack: DataPack = pipeline.process_one(data_path)

    for pack in Pipeline().set_reader(
            PlainTextReader()
    ).add(
        SpacyProcessor(), {"processors": ["sentence", "tokenize", "pos", "lemma", "ner"]}
    ).add( 
        StaveProcessor(), {
                    "port": 8880,
                    "project_name": "Meeting Notes Analyzer"
                }
    ).initialize().process_dataset(data_path):
        for sentence in pack.get("ft.onto.base_ontology.Sentence"):
            print("The sentence is: ", sentence.text)
            print("The entities are: ")
            for ent in pack.get("ft.onto.base_ontology.EntityMention", sentence):
                print(ent.text, ent.ner_type)