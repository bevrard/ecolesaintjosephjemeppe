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
})();
