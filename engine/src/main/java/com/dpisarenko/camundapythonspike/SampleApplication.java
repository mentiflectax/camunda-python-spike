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
    @Autowired
    private ProcessEngine engine;

    public static void main(String... args){
        // ScriptEngineManager.
        Options.importSite = false;
        final ScriptEngineManager manager = new ScriptEngineManager();
        final ScriptEngine engine = manager.getEngineByName("jython");

        SpringApplication.run(SampleApplication.class, args);
    }

    @PostConstruct
    public void test() {
        System.out.println("Hello");
    }
}
