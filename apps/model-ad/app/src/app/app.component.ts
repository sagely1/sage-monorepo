import { isPlatformServer } from '@angular/common';
import { Component, DestroyRef, inject, OnInit } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { RouterModule } from '@angular/router';
import { LOADING_ICON_COLORS } from '@sagebionetworks/explorers/constants';
import { MetaTagService, PlatformService } from '@sagebionetworks/explorers/services';
import { FooterComponent, HeaderComponent } from '@sagebionetworks/explorers/ui';
import { Dataversion, DataversionService } from '@sagebionetworks/model-ad/api-client-angular';
import { ConfigService, MODEL_AD_LOADING_ICON_COLORS } from '@sagebionetworks/model-ad/config';
import { footerLinks, headerLinks } from '@sagebionetworks/model-ad/util';
import {
  CONFIG_SERVICE_TOKEN,
  GoogleTagManagerComponent,
  createGoogleTagManagerIdProvider,
  isGoogleTagManagerIdSet,
} from '@sagebionetworks/shared/google-tag-manager';
import { ToastModule } from 'primeng/toast';

@Component({
  imports: [RouterModule, FooterComponent, HeaderComponent, ToastModule, GoogleTagManagerComponent],
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
  providers: [
    {
      provide: CONFIG_SERVICE_TOKEN,
      useFactory: () => inject(ConfigService),
    },
    {
      provide: LOADING_ICON_COLORS,
      useValue: MODEL_AD_LOADING_ICON_COLORS,
    },
    createGoogleTagManagerIdProvider(),
  ],
})
export class AppComponent implements OnInit {
  private platformService = inject(PlatformService);
  private destroyRef = inject(DestroyRef);
  configService = inject(ConfigService);
  dataVersionService = inject(DataversionService);
  metaTagService = inject(MetaTagService);

  readonly useGoogleTagManager: boolean;

  dataVersion = '';

  headerLinks = headerLinks;
  footerLinks = footerLinks;

  constructor() {
    this.metaTagService.initialize('Model AD');

    this.useGoogleTagManager = isGoogleTagManagerIdSet(
      this.configService.config.googleTagManagerId,
    );
  }

  ngOnInit() {
    this.getDataVersion();
  }

  getDataVersion() {
    if (this.platformService.isBrowser) {
      this.dataVersionService
        .getDataversion()
        .pipe(takeUntilDestroyed(this.destroyRef))
        .subscribe({
          next: (data) => {
            this.dataVersion = this.formatDataVersion(data);
          },
          error: (error) => console.error('Error loading data version:', error),
        });
    }
  }

  formatDataVersion(dataVersion: Dataversion) {
    return `${dataVersion.data_file}-v${dataVersion.data_version}`;
  }
}
