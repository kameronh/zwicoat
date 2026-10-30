// Play while on screen, pause off screen. With reduced motion, keep the poster and show controls.
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const vids = document.querySelectorAll<HTMLVideoElement>('video[data-loop]');
  const io =
    'IntersectionObserver' in window && !reduce
      ? new IntersectionObserver(
          (entries) => {
            entries.forEach((e) => {
              const v = e.target as HTMLVideoElement;
              if (e.isIntersecting) v.play().catch(() => {});
              else v.pause();
            });
          },
          { threshold: 0.15 },
        )
      : null;
  vids.forEach((v) => {
    if (reduce) {
      v.removeAttribute('autoplay');
      v.pause();
      v.controls = true;
    } else {
      io?.observe(v);
    }
  });
