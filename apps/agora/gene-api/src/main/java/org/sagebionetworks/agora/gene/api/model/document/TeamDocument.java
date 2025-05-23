package org.sagebionetworks.agora.gene.api.model.document;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document(collection = "teaminfo")
public class TeamDocument {

  @Id
  public String id;

  // XXX: Team.name would be better than Team.team (used in agora-api)
  private String team;
}
