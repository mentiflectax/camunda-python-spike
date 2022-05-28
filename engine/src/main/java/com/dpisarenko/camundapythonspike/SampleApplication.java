package com.dpisarenko.camundapythonspike;

import org.camunda.bpm.spring.boot.starter.annotation.EnableProcessApplication;
import org.python.core.Options;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableProcessApplication
public class SampleApplication {
    public static void main(String... args){
        Options.importSite = false;
        SpringApplication.run(SampleApplication.class, args);
    }
}
