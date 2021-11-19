import sys
sys.path.insert(1, 'C:/Users/colin/Documents/GitHub/fhdc/src/fhdc')

from fhdc_model import FHDC_Model

def main():
    
    docs = {
        0: "one one one two",
        1: "one one one three",
        2: "two two three three"
    }
    """
    docs = {
        0: 'Hello my name is Colin. Did I tell you my name?', 
        2:"I'm fun and    cool, hello!", 
        7:'Just a normal 98-year old! 700ppm. Normal Normal... and old.', 
        8:'What is a name? Years of old old sounds and repeated symbols...',
        3:'I I I have repeated repeated my90 self my..'
    }
    """

    model = FHDC_Model()

    corpus, vocabulary = model.preprocess(docs, return_processed=True)

    print()
    print('Corpus')
    print(corpus)
    document = 0
    print(f'Document {document}')
    print(corpus.docs[document].__str__(vocabulary=vocabulary))
    print('Vocabulary')
    print(vocabulary)
    print()

    model.cluster()

    print('Clustering Summary')
    print('Verbosity = 0')
    print(model.summary(verbosity=0))
    print('Verbosity = 1')
    print(model.summary(verbosity=1))
    print('Verbosity = 2')
    print(model.summary(verbosity=2))
    
    return

if __name__ == '__main__':
    main()
