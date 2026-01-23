# validate.py
import pickle, sys

try:
    pickle.load(open("movies_dict.pkl", "rb"))
    pickle.load(open("similarity.pkl", "rb"))
    print("Logic OK")
except Exception as e:
    print("Validation failed:", e)
    sys.exit(1)

