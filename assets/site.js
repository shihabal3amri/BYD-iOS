'use strict';

const copyButton = document.getElementById('copy-source');
copyButton.addEventListener('click', async () => {
  const field = document.getElementById('source-url');
  const status = document.getElementById('copy-status');
  try {
    await navigator.clipboard.writeText(field.value);
    status.textContent = copyButton.dataset.success;
  } catch {
    field.focus();
    field.select();
    status.textContent = copyButton.dataset.fallback;
  }
});
