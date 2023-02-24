import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UiModule } from '@sagebionetworks/openchallenges/ui';
import { OrgProfileOverviewComponent } from './org-profile-overview.component';

@NgModule({
  declarations: [OrgProfileOverviewComponent],
  imports: [CommonModule, UiModule],
  exports: [OrgProfileOverviewComponent],
})
export class OrgProfileOverviewModule {}