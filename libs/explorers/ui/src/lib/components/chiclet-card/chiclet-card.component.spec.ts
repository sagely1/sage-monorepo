import { By } from '@angular/platform-browser';
import { Chiclet } from '@sagebionetworks/explorers/models';
import { render, screen } from '@testing-library/angular';
import { ChicletComponent } from '../chiclet/chiclet.component';
import { ChicletCardComponent } from './chiclet-card.component';

describe('ChicletCardComponent', () => {
  const chiclets: Chiclet[] = [
    { label: 'PAK1', color: '#4caf50' },
    { label: 'chr1:109.8Mb', color: '#3f51b5' },
    { label: 'rs1801133', color: '#009688' },
  ];

  it('should render the title', async () => {
    await render(ChicletCardComponent, {
      inputs: { title: 'Example searches', chiclets },
    });
    expect(screen.getByText('Example searches')).toBeInTheDocument();
  });

  it('should render all chiclets', async () => {
    await render(ChicletCardComponent, {
      inputs: { title: 'Example searches', chiclets },
    });
    expect(screen.getByText('PAK1')).toBeInTheDocument();
    expect(screen.getByText('chr1:109.8Mb')).toBeInTheDocument();
    expect(screen.getByText('rs1801133')).toBeInTheDocument();
  });

  it('should forward label and color from each Chiclet model into ChicletComponent inputs', async () => {
    const { fixture } = await render(ChicletCardComponent, {
      inputs: { title: 'Example searches', chiclets },
    });
    const instances = fixture.debugElement
      .queryAll(By.directive(ChicletComponent))
      .map((debugEl) => debugEl.componentInstance as ChicletComponent);
    expect(instances).toHaveLength(chiclets.length);
    instances.forEach((instance, i) => {
      expect(instance.label()).toBe(chiclets[i].label);
      expect(instance.backgroundColor()).toBe(chiclets[i].color);
      expect(instance.textColor()).toBe('white');
    });
  });
});
