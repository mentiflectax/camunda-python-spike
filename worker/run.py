import logging
from concurrent.futures.thread import ThreadPoolExecutor
from camunda.external_task.external_task_worker import ExternalTaskWorker

default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30
}

def sample_external_task(task: ExternalTask) -> TaskResult:
    print("sample_external_task")
    return task.complete({"varFromPython": "Greetings from Python"})

def main():
    print("Starting the worker")
    ExternalTaskWorker(worker_id="1", config=default_config).subscribe("sample_external_task", sample_external_task)

if __name__ == '__main__':
    main()   
