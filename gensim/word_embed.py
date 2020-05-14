import spacy
from scipy.spatial.distance import cosine

# load word embedding model
nlp= spacy.load("en")

# define word embedding vectors
sponge_vec= nlp("sponge").vector

starfish_vec= nlp("starfish").vector

squid_vec = nlp("squid").vector

# compare vectors with cosine distance

dist_sponge_star= cosine(sponge_vec, starfish_vec)
dist_sponge_squid= cosine(sponge_vec, squid_vec)
dist_star_squid = cosine(starfish_vec, squid_vec)



