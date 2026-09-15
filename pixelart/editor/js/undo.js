// Full-snapshot undo. A 36x24 state is under 200 bytes, so 100 steps of
// mask + explicit copies beat any diff scheme at this canvas size.

export class Undo {
  constructor(limit = 100) {
    this.limit = limit;
    this.past = [];
    this.future = [];
  }

  // w/h travel with the snapshot so canvas resize is undoable
  snapshot(state) {
    return {
      w: state.w,
      h: state.h,
      mask: new Uint8Array(state.mask),
      explicit: new Map(state.explicit),
      base: state.base,
    };
  }

  push(state) {
    this.past.push(this.snapshot(state));
    if (this.past.length > this.limit) this.past.shift();
    this.future.length = 0;
  }

  // restore the last snapshot, stashing the current state for redo
  undo(state) {
    const snap = this.past.pop();
    if (!snap) return false;
    this.future.push(this.snapshot(state));
    this.restore(state, snap);
    return true;
  }

  redo(state) {
    const snap = this.future.pop();
    if (!snap) return false;
    this.past.push(this.snapshot(state));
    this.restore(state, snap);
    return true;
  }

  restore(state, snap) {
    state.w = snap.w;
    state.h = snap.h;
    state.mask = snap.mask;
    state.explicit = snap.explicit;
    state.base = snap.base;
  }
}
