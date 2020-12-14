# Reading and Writing Data with Azure Machine Learning

This repo is meant to address the common client question "How can I read and write data from Azure storage?" as part of the data science process using the Azure Machine Learning (AML) platform.

## Pre-requisites

* AML Workspace: [Create and Manage AML Workspaces](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=azure-portal)
* AML Compute Instance: [Create and manage an AML compute instance](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-manage-compute-instance?tabs=azure-studio)
* AML Compute Cluster: [Create an AML compute cluster](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-attach-compute-cluster?tabs=python)

## Steps

1.  Open the [AML Studio](https://ml.azure.com) open in a web browser
2.  From the left-hand navigation click `Notebooks`
3.  Click the `Open terminal` icon to open a terminal on the Compute Instance

![alt text](./instructions/media/open-terminal.png "Open terminal")

4.  From the terminal, clone the repo to the remote file share storage for the AML Workspace

    ```
        git clone https://github.com/sqlmartini/aml-read-write.git
    ```
5.  Review `read-write.py`
    * The `input_data_path` argument is the path to where the input data files are to be read in
    * The `output_data_path` argument is the path to where the output file is to written to
    * The sample csv file is read into a pandas dataframe from the `input_data_path` argument
    * The `output_data_path` directory is created if it doesn't already exist
    * The pandas dataframe is written in csv format to the `output_data_path`

6.  Review `aml_confgi/read-write.runconfig` YAML file
    * test