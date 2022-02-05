# Movie Recommendations Project

_W2022 MDST Project: Building a Movie Recommender System_

## Table of Contents

-   [Introduction](#introduction)
-   [Description](#description)
-   [Goals](#goals)
-   [Stretch Goals](#stretch-goals)
-   [A Look at the Data](#a-look-at-the-data)
-   [Project Roadmap](#project-roadmap)
-   [Setup](#setup)
-   [A Tour of the Repository](#a-tour-of-the-repository)
-   [Relevant Links](#relevant-links)

## Introduction

What do you do when you want to watch a movie, but don't know what to watch? Like... _really_ don't know what to watch? What drives your decision-making for watching a particular movie?

-   Did a friend suggest it to you?
-   Do you google [watchlists](https://www.google.com/search?q=movies+to+watch&oq=movies+to+watch)?
-   Maybe you take [buzzfeed quizzes](https://www.buzzfeed.com/tag/movie-recommendations) for recommendations?

If you ever felt unsatisfied with movie recommendation engines, or just want to learn more about how they work, then this is the project for you!

## Description

The goal of this project is to make a functional recommender system and learn how and why it recommends the movies it does. The two main kinds of recommender systems we plan to explore are content-based and collaborative filtering (more information can be found [here](https://analyticsindiamag.com/collaborative-filtering-vs-content-based-filtering-for-recommender-systems/)). These programs will be used as engines to drive an online quiz (similar to [buzzfeed quizzes](https://www.buzzfeed.com/tag/movie-recommendations)) to give ~10 movie recommendations.

Here are some of the relevant data science buzzwords and jargon for this project!

-   Regression
-   (Un)supervised Learning
-   K-Nearest Neighbors
-   Matrix Factorization (Asymmetric SVD)
-   Naive Bayes
-   Recommender System

## Goals

1. Design a functional recommender system from scratch and gain insight to their
   mechanics
2. Provide MDST members the opportunity to work with recommender systems that are very
   prevalent in industry
3. Have a user interface (form of a website)
4. Have fun and learn something! 😃

## Stretch Goals

1. Augment movie preferences with Bayesian conditional probability scores
2. Test recommender systems on larger datasets
3. Incorporate nonrating data along side ratings to boost prediction performance
4. Predict genre from movie preferences by analyzing latent factors

## A Look at the Data

The data is from the [Movie Lens | Group Lens dataset](https://grouplens.org/datasets/movielens/). The dataset can also be obtained through [TensorFlow](https://www.tensorflow.org/datasets/catalog/movielens). The main focus will be on the 100k dataset. **You will not have to download the dataset directly, the [Setup](#setup) section has directions for fetching the dataset.**

## Project Roadmap

Week of **1/30**: Learn Our Data

-   Kickoff!
-   Introductions
-   Exploratory Data Analysis

---

Week of **2/6**: Methodology

-   Data cleaning
-   More EDA
-   Basic modeling
-   Introduction to algorithms (kNN, Matrix Factorization)

---

Weeks of **2/13-3/13**: Build Models

-   Sub-teams!
-   In-depth analysis of algorithms
-   Development of algorithm specification
-   Building, training, and testing models
-   Create visualizations

---

## **2/26-3/5**: _Spring Break!_

---

Week of **3/20-3/27**: Refine Models

-   Evaluate and run models
-   Preliminary results
-   Create visualizations

---

Week of **3/27-4/3**: Develop Quiz Application

-   Plan out application design
-   Flesh out basic API to interact with webpage
-   Test it!

---

Week of **4/10**: Finishing Touches

-   Complete the write-up
-   Final Presentations!

## Setup

Getting all setup to contribute to this project is as simple as a few commands.

### Virtual Environment

The first step is to initialize the virtual environment with all the required packages. Luckily, this isn't too hard.

First create a Python 3.8 virtual environment. The virtual environment creation code for Linux/MacOS is below:

```bash
python3.8 -m venv venv
```

After activating the virtual environment (this will depend on your system), install the required dependencies using

```bash
pip install -r requirements.txt
```

If you also want to install dependencies of the development environment like code formatters and Jupyter notebook, run

```bash
pip install -r requirements-dev.txt
```

### Obtaining the Data

**Note: You only need to download the data if you are unable to use TensorFlow Datasets to do so. If you are able to access the `tensorflow_datasets` package, you can skip this section and get started working!**

Getting the MovieLens dataset this project utilizes is not too difficult as well. With your virtual environment activated, run

```bash
python setup.py
```

That's all! You'll find the extracted dataset in the `data` folder. If you'd like more control over where you want to download and extract the dataset, use the `download` and `extract` options:

```bash
python setup.py --download <custom_filepath> --extract <custom_filepath> <custom_extraction_dir>
```

All download options can be viewed using

```bash
python setup.py --help
```

## Relevant Links

[MDST Calendar](https://www.mdst.club/agenda)

Dataset:

-   [Movie Lens | Group Lens](https://grouplens.org/datasets/movielens/)
-   via [TensorFlow](https://www.tensorflow.org/datasets/catalog/movielens)

Resources:

-   [Collaborative Filtering and Content-Based Filtering](https://analyticsindiamag.com/collaborative-filtering-vs-content-based-filtering-for-recommender-systems/)
-   [K-NN](https://www.youtube.com/watch?v=HVXime0nQeI)
-   [Matrix Factorization](https://www.youtube.com/watch?v=ZspR5PZemcs)
-   [Naive Bayes](https://www.youtube.com/watch?v=O2L2Uv9pdDA)
-   [Andrew Ng's Review on Recommender Systems - Lectures 16.1-16.6](https://www.youtube.com/watch?v=giIXNoiqO_U&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=96)
