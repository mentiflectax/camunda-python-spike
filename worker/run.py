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


def provoke_technical_failure(task: ExternalTask) -> TaskResult:
    return task.failure(error_message="Technical error occurred",  error_details="Demonstration of simulating a technical error", max_retries=0, retry_timeout=5000)

def order_item_from_warehouse(task: ExternalTask) -> TaskResult:
    return task.bpmn_error(error_code="Out of stock", error_message="Item X is not available at the moment.", variables={"var1": "value1", "success": False})

def main():
    configure_logging()
    topics = [
        ("sample_external_task", sample_external_task),
        ("determine_type_of_customer", determine_type_of_customer),
        ("provoke_technical_failure", provoke_technical_failure),
        ("order_item_from_warehouse", order_item_from_warehouse)
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
