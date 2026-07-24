import { BreakpointObserver } from '@angular/cdk/layout';
import { Component, computed, inject, signal } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import {
  HomeCardComponent,
  SvgImageComponent,
  ToggleCardComponent,
  ToggleCardOption,
} from '@sagebionetworks/explorers/ui';
import { isModelOrganism, ModelOrganism, ROUTE_PATHS } from '@sagebionetworks/model-ad/config';
import { SearchInputComponent } from '@sagebionetworks/model-ad/ui';

interface Stat {
  label: string;
  value: string;
}

@Component({
  selector: 'model-ad-home',
  imports: [ToggleCardComponent, HomeCardComponent, SvgImageComponent, SearchInputComponent],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent {
  private readonly breakpointObserver = inject(BreakpointObserver);

  // Must match $home-mobile-md-max-width in home.component.scss
  private readonly MOBILE_BREAKPOINT = 850;

  // The hero arc is split into an upper decorative arc (anchored to the top of the page) and a
  // lower arc that sits behind the stats, tracking them regardless of the content height above
  // (which changes with the selected model organism). Each breakpoint uses its own artwork.
  private readonly upperArcImageDesktop = 'model-ad-assets/images/home-arc-bg-upper.svg';
  private readonly upperArcImageMobile = 'model-ad-assets/images/home-arc-bg-upper-mobile.svg';
  private readonly lowerArcImageDesktop = 'model-ad-assets/images/home-arc-bg-lower.svg';
  private readonly lowerArcImageMobile = 'model-ad-assets/images/home-arc-bg-lower-mobile.svg';

  private readonly isMobile = signal(false);

  readonly upperArcImage = computed(() =>
    this.isMobile() ? this.upperArcImageMobile : this.upperArcImageDesktop,
  );
  readonly lowerArcImage = computed(() =>
    this.isMobile() ? this.lowerArcImageMobile : this.lowerArcImageDesktop,
  );

  readonly selectedModelOrganism = signal<ModelOrganism>('mouse');

  readonly modelOrganismOptions: (ToggleCardOption & { value: ModelOrganism })[] = [
    {
      label: 'Mouse Models',
      value: 'mouse',
      imagePath: 'model-ad-assets/images/mouse-with-brain-network.svg',
      imageAltText: 'mouse model icon',
    },
    {
      label: 'Marmoset Models',
      value: 'marmoset',
      imagePath: 'model-ad-assets/images/marmoset-model.svg',
      imageAltText: 'marmoset model icon',
    },
  ];

  ROUTE_PATHS = ROUTE_PATHS;

  setModelOrganism(value: string | undefined) {
    if (isModelOrganism(value)) {
      this.selectedModelOrganism.set(value);
    }
  }

  stats: Stat[] = [
    {
      label: 'Institutions',
      value: '5+',
    },
    {
      label: 'Genes',
      value: '20K+',
    },
    {
      label: 'Models',
      value: '15+',
    },
  ];

  constructor() {
    this.breakpointObserver
      .observe([`(width < ${this.MOBILE_BREAKPOINT}px)`])
      .pipe(takeUntilDestroyed())
      .subscribe((result) => this.isMobile.set(result.matches));
  }
}
