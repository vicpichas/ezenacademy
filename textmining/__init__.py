from textmining.model import SamsungReport

if __name__ == '__main__':
    sam = SamsungReport()
    # vsam.download()
    print(sam.draw_wordcloud())