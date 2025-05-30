### AirBnB clone project

## Project Description

This repository contains the initial phase of our project to build a clone of the AirBnB web application. In this stage, we focus on developing a command-line interface (CLI) that serves as the backend management system for the application's data.

We'll be implementing a command interpreter to manage different objects that represent AirBnB components.

We will:

Create a parent class *BaseModel* to handle initialization, serialization, and deserialization of instances

Set up a flow for converting between objects and persistent storage:
Instance ↔ Dictionary ↔ JSON string ↔ File

Build subclasses such as `User`, `State`, `City`, `Place`, and others, all inheriting from *BaseModel*

Develop a file-based storage engine to store and retrieve serialized data

Write unit tests for each class and component to ensure reliability and correctness

The command interpreter will be able to:

Create new instances of objects (e.g., `User`, `Place`)

Retrieve stored objects

Update existing objects with new attributes

Count instances or perform data-based operations

Delete objects from storage

Persistent data storage is achieved using JSON serialization, ensuring that data remains intact between sessions.