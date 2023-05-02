from roku import Roku


def launch_and_search_in_youtube(roku: Roku, keyword: str):
    """
    TODO
    """
    roku["YouTube"].launch()
    [roku.left() for i in range(10)]
    [roku.up() for i in range(15)]
    roku.down()
    roku.select()
    # [roku.backspace() for i in range(10)]
    roku.literal(keyword)
    roku.select()
    [roku.down() for i in range(1)]
    return roku
