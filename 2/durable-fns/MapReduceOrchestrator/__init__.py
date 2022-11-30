# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    output = []

    #get text from blob
    dataset = yield context.call_activity('GetInputData')

    #Mapper
    tasks = [context.call_activity('MapperActivity', data) for data in dataset]
    mapping = yield context.task_all(tasks)

    #Shuffler
    shuffler_input = list()
    for shuffle_list in mapping:
        for item in shuffle_list:
            shuffler_input.append(item)
    shuffler_output = yield context.call_activity('ShufflerActivity', shuffler_input)

    #Reducer
    tasks = [context.call_activity('ReducerActivity', shuffler) for shuffler in shuffler_output] 
    output = yield context.task_all(tasks)
    
    return output

main = df.Orchestrator.create(orchestrator_function)
