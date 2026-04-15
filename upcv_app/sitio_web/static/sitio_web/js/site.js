document.querySelectorAll('.counter').forEach((el)=>{
  const target = Number(el.dataset.value || 0);
  let current = 0;
  const step = Math.max(1, Math.round(target / 50));
  const intv = setInterval(() => {
    current += step;
    if (current >= target) {
      el.textContent = target;
      clearInterval(intv);
      return;
    }
    el.textContent = current;
  }, 22);
});
