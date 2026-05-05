import { Component, input, model, output } from '@angular/core';
import { ComparisonToolFilterOption } from '@sagebionetworks/explorers/models';
import { ChicletComponent } from '@sagebionetworks/explorers/ui';

@Component({
  selector: 'explorers-comparison-tool-filter-list-item',
  standalone: true,
  imports: [ChicletComponent],
  templateUrl: './comparison-tool-filter-list-item.component.html',
  styleUrls: ['./comparison-tool-filter-list-item.component.scss'],
})
export class ComparisonToolFilterListItemComponent {
  item = input<ComparisonToolFilterOption | null>();
  title = input<string>('');
  description = input<string>('');

  isVisible = model<boolean>(false);

  clearEvent = output<object>();

  clearWasClicked() {
    this.isVisible.set(false);
    this.clearEvent.emit(this.item() ?? {});
  }
}
