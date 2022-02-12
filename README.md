# Project Name: Which Bollywood Celebrity You look like

A Deep learning based streamlit web app which can tell with which bollywood celebrity your face resembles.

Face recognition is the problem of identifying and verifying people in a photograph by their face.
It is a task that is trivially performed by humans, even under varying light and when faces are changed by age or obstructed with accessories and facial hair. Nevertheless, it is remained a challenging computer vision problem for decades until recently.

Deep learning methods are able to leverage very large datasets of faces and learn rich and compact representations of faces, allowing modern models to first perform as-well and later to outperform the face recognition capabilities of humans.

In this project, you will discover the problem of face recognition and how deep learning methods can achieve superhuman performance to identify similar faces.


## Demo Video:
![ezgif-1-1ca55b365e](https://user-images.githubusercontent.com/75604769/153721961-8143fab4-897c-471b-b0c1-d2b6fd55fd92.gif)

This is a methods of identifying similar faces check various aspects on pictures, including: face shape, nose, eyes and mouth; face position in the picture; skin color (including the lighting of the photo); color and hair and cosine_similarity.

# Dataset has been used:
https://www.kaggle.com/sushilyadav1998/bollywood-celeb-localized-face-dataset


# Some Real Time Demo:

Web app look

<img src="demo/1.png" alt="workflow" width="70%">

Lets check some of images

<img src="demo/2.png" alt="workflow" width="70%">

<img src="demo/3.png" alt="workflow" width="70%">

This really performing good you can consider by seeing this result 😀

<img src="demo/4.png" alt="workflow" width="70%">

The fun part is I am looked like Riteish Deshmukh 😄😁

<img src="demo/5.png" alt="workflow" width="70%">

# STEPS to run this project:

You can also use others images instead of bollywood actress

## STEP 01: 
Clone the repository

```bash
git clone https://github.com/entbappy/Which-Bollywood-Celebrity-You-look-like.git
```

## STEP 02: 
Create an environment


```bash
conda create -n celebrity python=3.7 -y
```

## STEP 03: 
Install the requirements


```bash
pip install -r requirements.txt
```

## STEP 04: 
Download the data from the link and keep it in your project directory. Make sure all the actress folder should be in just one folder called data, like that

<img src="demo/data.png" alt="workflow" width="70%">

## STEP 05: 
Just execute this command one time if you are not changing the data


```bash
python run.py
```

## STEP 06: 
Now to start the webapp run the following command


```bash
streamlit run app.py
```

yes!! Now you can start predicting 🙂

# Authors:
```bash
Author: Dipesh Silwal
ML Engineer
Email: dipeshsilwal31@gmail.com
```


