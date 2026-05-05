import { screen, within } from '@testing-library/angular';

/**
 * Finds the remove (close) button inside the `<explorers-chiclet>` whose
 * label text matches `labelMatcher`. Useful when multiple chiclets are on
 * screen and `getByRole('button')` would be ambiguous.
 */
export function getChicletRemoveButton(labelMatcher: string | RegExp): HTMLElement {
  const labelEl = screen.getByText(labelMatcher, { exact: false });
  const chicletHost = labelEl.closest('explorers-chiclet') as HTMLElement | null;
  if (!chicletHost) {
    throw new Error(`No explorers-chiclet host found for label ${labelMatcher}`);
  }
  return within(chicletHost).getByRole('button');
}
