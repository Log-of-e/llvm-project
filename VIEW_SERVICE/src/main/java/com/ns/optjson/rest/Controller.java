package com.ns.optjson.rest;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FilenameFilter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import org.springframework.beans.factory.annotation.Value;

import org.springframework.web.bind.annotation.CrossOrigin;


@CrossOrigin( origins = "*" )
@RestController
public class Controller {

    @Value("${filedir}")
    String dir;


    @GetMapping(value = "/process/{llfile}", produces={"application/json"}, headers = "Content-type=application/json")
    @ResponseBody
    public String fileanalysis(@PathVariable String llfile) throws FileNotFoundException, SecurityException, OutOfMemoryError, IOException  {

        try {

            Path _path =  Paths.get(dir,llfile+ ".ll.json");
            String contents = Files.readString(_path, StandardCharsets.ISO_8859_1);
            return contents;
                
        } catch (Exception e) {
            //TODO: handle exception
            return "{\"file\":\"not found\"}";
        }
    }
    
    @GetMapping(value="/file_list", headers = "Content-type=application/json")
    @ResponseBody
    public String[] filelisting() {

        String[] pathnames;
        File f = new File(dir);

        FilenameFilter filter = new FilenameFilter() {
            @Override
            public boolean accept(File f, String name) {
                return name.endsWith(".ll");
            }
        };
    
        pathnames = f.list(filter);

        return pathnames;
    }
}