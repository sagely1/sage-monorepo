import { Component, Input, OnInit } from '@angular/core';
import {
  Challenge,
  ChallengePlatformService,
  SimpleChallengePlatform,
} from '@sagebionetworks/openchallenges/api-client-angular';
import { Challenge as DeprecatedChallenge } from '@sagebionetworks/openchallenges/api-client-angular-deprecated';
import { startCase } from 'lodash';

@Component({
  selector: 'openchallenges-challenge-card',
  templateUrl: './challenge-card.component.html',
  styleUrls: ['./challenge-card.component.scss'],
})
export class ChallengeCardComponent implements OnInit {
  @Input() challenge!: Challenge;
  // TODO: remove the deprecatedChallenge when real Challenge has all required properties
  @Input() deprecatedChallenge!: DeprecatedChallenge;
  platform!: SimpleChallengePlatform;
  status!: string | undefined;
  statusClass!: string;
  difficulty!: string | undefined;

  constructor(private challengePlatformService: ChallengePlatformService) {}

  ngOnInit(): void {
    if (this.challenge) {
      this.status = this.challenge.status ? this.challenge.status : 'No Status';
      this.statusClass = this.challenge.status || '';
      this.difficulty = this.challenge.difficulty
        ? startCase(this.challenge.difficulty.replace('-', ''))
        : undefined;
      this.platform = this.challenge.platform;
    }
  }

  // TODO: remove once the property to redirect to challenge page is determined
  snakeCase(value: string): string {
    return value.replace(/ /g, '-').toLowerCase();
  }
}