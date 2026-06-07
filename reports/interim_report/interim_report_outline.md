# Predictive Maintenance Capstone Project

## Cover Page
- Project Title: Predictive Maintenance
- Student Name: Gopikrishna Rajendran
- Program Name: PGP - AIML
- Submission Type: Interim Submission
- Date: 

## Table of Contents

# 1. Problem Statement

## Business Context

Vehicle breakdowns and engine failures lead to significant financial losses for both individual owners and fleet operators. Unexpected engine failures can cause expensive repairs, operational downtime, and safety risks. Predictive maintenance in the automotive industry can help minimize these issues by leveraging sensor data to forecast potential failures before they occur. 

Automobile manufacturers, fleet managers, and service providers aim to develop data-driven solutions to improve engine reliability and optimize maintenance schedules. By analyzing engine health parameters such as RPM, temperature, pressure, and other sensor readings, machine learning models can be trained to predict when an engine requires maintenance, allowing proactive intervention before a failure occurs. 

The sensor values in the dataset are consistent with the operating parameters of larger and small engines commonly found in equipment like Vehicles, lawnmowers, portable generators, and compact machinery. Some engines operate at lower RPMs, pressures, and temperatures compared to larger automotive engines and vice versa. Therefore, the data is appropriate for developing predictive maintenance models tailored to large and small engine applications. 

## Objective

As a Data Scientist, your goal is to build a predictive maintenance model that can analyze historical and real-time engine sensor data to identify potential failures. The model should accurately classify whether an engine requires maintenance or is operating normally. 

This solution will help:

- Reduce unplanned breakdowns and costly repairs.
- Improve vehicle performance and engine lifespan.
- Optimize maintenance schedules to minimize downtime
- Provide data-driven insights to manufacturers and fleet operators for better decision-making. 


# 2. Data Registration

## Dataset Source

The dataset used for this project consists of engine operational parameters collected for predictive maintenance analysis. The data includes sensor-based measurements related to engine performance and operating conditions.

The dataset is designed for machine learning classification tasks where the objective is to identify whether an engine requires maintenance or is operating normally.




## Hugging Face Dataset Repository

A Hugging Face Dataset Repository was created to manage and maintain dataset versions for this project.

- Dataset Repository Name: predictive-maintenance-dataset
- Dataset Repository Link: gkrishna4346/predictive-maintenance-dataset


- Model Repository Name: predictive-maintenance-model
- Model Repository Link: gkrishna4346/predictive-maintenance-model

Purpose:
- Store raw and processed datasets
- Enable dataset version tracking
- Support reproducibility
- Facilitate deployment and sharing


## Dataset Features Description

The dataset contains the following features:

- Engine RPM
- Lubrication Oil Pressure
- Fuel Pressure
- Coolant Pressure
- Lubrication Oil Temperature
- Coolant Temperature
- Engine Condition (Target Variable)

Target Variable:

Engine Condition represents the operational state of the engine and will be used for predictive classification.


# 3. Exploratory Data Analysis

## Dataset Overview

## Dataset Shape

## Data Types

## Missing Value Analysis

## Duplicate Analysis

## Statistical Summary

## Univariate Analysis

## Bivariate Analysis

## Multivariate Analysis

## Correlation Analysis

## Key Insights


# 4. Data Preparation

## Data Cleaning

## Feature Selection

## Feature Engineering

## Train-Test Split


# 5. Model Building with Experiment Tracking

## Baseline Model

## Model 1

## Model 2

## Model 3

## Hyperparameter Tuning

## Model Comparison

## Best Model Selection


# 6. Output Evaluation

## Accuracy

## Precision

## Recall

## F1 Score

## Confusion Matrix


# 7. Model Deployment

## Streamlit Application

## Docker Integration

## Hugging Face Deployment


# 8. Automated GitHub Actions Workflow

## Pipeline Architecture

## Workflow YAML


# 9. Actionable Insights and Recommendations


# 10. Conclusion


# Appendix

## Code Snippets

## Additional Graphs

## Screenshots