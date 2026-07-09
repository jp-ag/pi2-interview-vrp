# Incident Challenge: Buganizer Portal

## Section 0: Getting Started

You can run the Buganizer Triage Workbench locally either using Docker.

### Option A: Running with Docker 

1.  Build the Docker image from the project root directory:

    ```bash
    docker build -t buganizer-workbench .
    ```

2.  Run the container:

    ```bash
    docker run -d --network host --name buganizer-sim buganizer-workbench
    ```

3.  The server will start and listen on:
    -   `http://127.0.0.1:8081`: Serves the Issue Tracker portal, where you can view the reported issues (`/1` and `/2`).

4.  To stop and remove the running container when finished:

    ```bash
    docker stop buganizer-sim
    docker rm buganizer-sim
    ```

--------------------------------------------------------------------------------

## Section 1: Incident Report

We have received two external security reports that you have to triage.

Please review the details in [Issue 1](http://127.0.0.1:8081/1) and
[Issue 2](http://127.0.0.1:8081/2) to understand and analyze the findings.

You are being evaluated on your english writing, on your capabilities of 
understanding the rules, and asking and researching for any other meaningful
information that you need.

--------------------------------------------------------------------------------

## Section 2: Candidate Tasks

Your objective is to analyze the vulnerability reports and triage them according 
to the rules.
### Tasks

0.  **Read and understand the rules**
1.  **Analyze the reports and answer them** 




