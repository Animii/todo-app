import json
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('DATA_TABLE'))

def lambda_handler(event, context):
    operation = event.get('field')
    args = event.get('arguments')
 
    response = {}

    if operation == "createTodo":
        response = createToDo(args.get('createTodoInput'))
    elif operation == "updateTodo":
        response = updateToDo(args)
    elif operation == "readTodo":
        response = readTodo(args)
    elif operation == "listTodo":
        response = listTodo(args)
    elif operation == "deleteTodo":
        response = deleteToDo(args)

    return response

def createToDo(args):
    todo = {
       'id': uuid.uuid4().hex,
       'label': str(args.get('label','')),
       'ticked': False
    }

    response = table.put_item(
       Item=todo
    )

    return todo
 

def updateToDo(args):
    return {}

def readTodo(args):
    todoid = str(args.get('id'))

    try:
        response = table.get_item(Key={'id': todoid})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']

def listTodo(args):
    return {}