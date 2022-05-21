import logging
from camunda.external_task.external_task import ExternalTask, TaskResult
from concurrent.futures.thread import ThreadPoolExecutor
from camunda.external_task.external_task_worker import ExternalTaskWorker

default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30,
    "isDebug": True
}

def sample_external_task(task: ExternalTask) -> TaskResult:
    print("sample_external_task")
    return task.complete({"varFromPython": "Greetings from Python"})


def determine_type_of_customer(task: ExternalTask) -> TaskResult:
    print("determine_type_of_customer")
    customer_nr = task.get_variable("CUSTOMER_NUMBER")
    if ((customer_nr % 2) == 0):
        customer_type = "CORPORATE"
    else:
        customer_type = "INDIVIDUAL"
    return task.complete({"CUSTOMER_TYPE": customer_type})

def main():
    configure_logging()
    topics = [
        ("sample_external_task", sample_external_task),
        ("determine_type_of_customer", determine_type_of_customer)
    ]
    executor = ThreadPoolExecutor(max_workers=len(topics))
    for index, topic_handler in enumerate(topics):
        topic = topic_handler[0]
        handler_func = topic_handler[1]
        executor.submit(ExternalTaskWorker(worker_id=index, config=default_config, base_url="http://localhost:8081/engine-rest").subscribe, topic, handler_func)

def configure_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=[logging.StreamHandler()])
    
if __name__ == '__main__':
    main()   
