// -*- combobulate-test-point-overlays: ((1 outline 205) (2 outline 220) (3 outline 242) (4 outline 256)); eval: (combobulate-test-fixture-mode t); -*-

const test = () => (
  <something>
    <foo>
      <bar>quux</bar> <bar>baz</bar>
      {1 + 2}
      {3 + 4}
    </foo>
  </something>)