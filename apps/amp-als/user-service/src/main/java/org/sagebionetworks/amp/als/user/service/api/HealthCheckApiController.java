package org.sagebionetworks.amp.als.user.service.api;

import org.sagebionetworks.amp.als.user.service.model.dto.BasicErrorDto;
import org.sagebionetworks.amp.als.user.service.model.dto.HealthCheckDto;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.multipart.MultipartFile;

import jakarta.validation.constraints.*;
import jakarta.validation.Valid;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import jakarta.annotation.Generated;

@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", comments = "Generator version: 7.12.0")
@Controller
@RequestMapping("${openapi.aMPALSUserService.base-path:/v1}")
public class HealthCheckApiController implements HealthCheckApi {

    private final HealthCheckApiDelegate delegate;

    public HealthCheckApiController(@Autowired(required = false) HealthCheckApiDelegate delegate) {
        this.delegate = Optional.ofNullable(delegate).orElse(new HealthCheckApiDelegate() {});
    }

    @Override
    public HealthCheckApiDelegate getDelegate() {
        return delegate;
    }

}
