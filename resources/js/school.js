/* Progressive enhancement: all navigation and content works without JavaScript. */
(() => {
  document.body.classList.add('js');
  const menu = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('#navigation');
  menu.hidden = false;
  const setMenu = (open) => {
    menu.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
  };
  menu.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
  navigation.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      setMenu(false);
      menu.focus();
    }
  });
  const filters = document.querySelector('.news-filters');
  if (!filters) return;
  filters.hidden = false;
  const cards = [...document.querySelectorAll('.news-card')];
  const practical = ['Infos pratiques', 'Inscriptions'];
  filters.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-filter]');
    if (!button) return;
    const filter = button.dataset.filter;
    filters.querySelectorAll('button').forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
    let count = 0;
    cards.forEach((card) => {
      const category = card.dataset.category;
      const show = filter === 'all' || (filter === 'archives' && category === 'Archives') || (filter === 'practical' && practical.includes(category)) || (filter === 'school' && category !== 'Archives' && !practical.includes(category));
      card.hidden = !show;
      if (show) count += 1;
    });
    document.querySelector('.filter-status').textContent = `${count} actualité${count > 1 ? 's' : ''} affichée${count > 1 ? 's' : ''}.`;
  });
})();
