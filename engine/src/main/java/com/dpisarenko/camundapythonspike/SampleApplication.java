package com.dpisarenko.camundapythonspike;

import org.camunda.bpm.spring.boot.starter.annotation.EnableProcessApplication;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableProcessApplication
public class SampleApplication {
    public static void main(String... args){
        SpringApplication.run(SampleApplication.class, args);
    }
}
