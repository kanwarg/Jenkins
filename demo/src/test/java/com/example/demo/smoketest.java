package com.example.demo;
import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Test;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.AutoConfiguration;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
@AutoConfiguration
public class smoketest {
    
@Autowired
    private HomeController ctl;
    
    @Test
	public void contextLoads()  {
		assertThat(ctl).isNotNull();
	}

}
