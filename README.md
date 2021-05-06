# Document Similarity evaluator [Flask + Docker + Heroku]

In this repository, we traverse through the essential building blocks of a Machine Learning/Deep Learning project in production, i.e. a model that end users can actually interact with.

We create a simple document similarity evaluation tool, which determines how similar two documents are to each other. We use the `nltk` library, and tools from `sklearn` (TfidfVectorizer, cosine-similarity) to achieve the same.

The webpage is hosted on Heroku and can be accessed here: [link](https://docapp-sbh.herokuapp.com/)

This project consists of the following parts:

## Build the Similarity Evaluator : (Tfidf, Cosine Similarity)

[similarity.py](./similarity.py) describes how to determine the similarity between two sentences/documents.

## Create API : Flask

<p align="center">
<img src="https://user-images.githubusercontent.com/12089275/117300654-0ea6fd00-ae7a-11eb-9967-071aaec8a818.png" alt="flask logo" width="240" height="240">
</p>



[app.py](./app.py) contains the code for running the API. It interacts with the [web page](./templates/landing_page.html) where the user provides the texts corresponding to two different documents.

## Containerize : Docker

<p align="center">
<img src="https://user-images.githubusercontent.com/12089275/117300859-48780380-ae7a-11eb-8b71-4da15554bc8c.png" alt="docker logo" width="240" height="240">
</p>

Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package.

To dockerize our application, we need to :

**1.** [Download and install Docker](https://www.docker.com/products/docker-desktop)

**2.** Create the [requirements.txt](./requirements.txt) in our main directory

**3.** Create a [Dockerfile](./Dockerfile) which contains the instructions for building the Docker image

**4.** In a terminal, run the following command to build the Docker image:
  ```
  > docker build -f Dockerfile -t docapp .
  ```

**5.** Run container in background and print container ID using:
```
> docker run -p 5000:5000 -d docapp
```

Once this is running, the app can be viewed on the browser at:
```
http://localhost:5000/
```

## Deploy : Heroku

<p align="center">
<img src="https://user-images.githubusercontent.com/12089275/117300731-21b9cd00-ae7a-11eb-819f-6e7de9bbf140.png" alt="heroku logo" width="240" height="100">
</p>

[Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the Cloud.

**1.** Create a new [Heroku account](https://signup.heroku.com/). Then download the Heroku [Command Line Interface (CLI)](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) which allows us to create and manage our Heroku apps directly from the terminal.

**2.** Login to the Heroku account using `> heroku login`

**3.** Log in to Container Registry: `> heroku container:login`

**4.** Create a new Heroku app: `> heroku create <app-name>`

**5.** Build the image based on your Dockefile and push it to this particular app in Heroku `> heroku container:push web --app <app-name>`

**6.** After an image is pushed to the Container Registry, we can create a new release using `> heroku container:release web`

**7.** We can finally launch our Heroku application through the command `> heroku open --app <app-name>`


## Screenshot

![image](https://user-images.githubusercontent.com/12089275/117305133-c211f080-ae7e-11eb-88cd-76058d9d202d.png)

