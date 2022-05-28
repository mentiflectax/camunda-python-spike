package com.dpisarenko.camundapythonspike;

import org.camunda.bpm.engine.ProcessEngine;
import org.camunda.bpm.spring.boot.starter.annotation.EnableProcessApplication;
import org.python.core.Options;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import javax.annotation.PostConstruct;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineFactory;
import javax.script.ScriptEngineManager;

@SpringBootApplication
@EnableProcessApplication
public class SampleApplication {
    public static void main(String... args){
        Options.importSite = false;
        SpringApplication.run(SampleApplication.class, args);
    }
}
