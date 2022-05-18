import random

articles = ["a", "the", "one", "some"]
nouns = ["apple", "carrot", "rabbit", "banana", "basketball", "chess", "sun", "wind"]
verbs = ["cooks", "blows", "bounces", "walks", "jumps", "calls", "stays", "runs", "abides"]
conjunctions = ["for", "and", "nor", "but", "yet", "so"]
dependent_clause_markers = ["although", "even if", "until", "when", "whether", "while", "in order to"]
clauses = ["after", "while", "if", "as", "where", "even", "though"]

def independent_clause():
    return random.choice(articles) + " " + random.choice(nouns) + " " + random.choice(verbs)

def dependent_clause():
    return random.choice(dependent_clause_markers) + " " + independent_clause()

def simple_sentence():
    return independent_clause() + "."
     
    #compound sentences = ind.clause + random conjunction + ind.clause
    # call upon ind.clause function, add space, conjunction, and another space and add additional ind.clause
    #add period at end.
    
def compound_sentence(): 
    return independent_clause() + " " + random.choice(conjunctions) + " " + independent_clause() + "."
    
    #dependent marker plus clause plus independent clause
    #call dep.clause, space, random clause, space, call ind.clause, add period.
    
def complex_sentence(): 
    return dependent_clause() + " " + random.choice(clauses) + " " + independent_clause() + "."
    
    #dependent clause plus independent clause plus coordinating conjunction plus independent clause
    #call dep.clause, space, call ind.clause, space, random conjunc., space, call ind.clause, add period.
    
def compound_complex_sentence(): 
    return dependent_clause() + " " + independent_clause() + " " + random.choice(conjunctions) + " " + independent_clause() + "."





if __name__ == "__main__":
    #test print for simple sentence
    sentence = simple_sentence()
    print(sentence)
    #test print for compound sentence
    compound_sentence = compound_sentence()
    print(compound_sentence)
    #test print for complex sentence
    complex_sentence = complex_sentence()
    print(complex_sentence)
    #test print for compound-complex sentence
    compound_complex_sentence = compound_complex_sentence()
    print(compound_complex_sentence)
