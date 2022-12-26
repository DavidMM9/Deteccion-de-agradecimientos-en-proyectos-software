from grobid_client.grobid_client.grobid_client import GrobidClient


def useGrobid(input, output):
    client = GrobidClient(config_path="./config.json")
    client.process("processFulltextDocument", input, output, force=True, verbose=False)
