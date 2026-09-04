from langchain_community.utilities import GoogleSerperAPIWrapper


def get_tools():

    search = GoogleSerperAPIWrapper()

    return [
        search.run
    ]