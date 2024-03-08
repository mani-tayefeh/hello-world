from tqdm import tqdm
from time import sleep

for char in tqdm(range(100),colour="RED",ncols=50):
    sleep(0.25)