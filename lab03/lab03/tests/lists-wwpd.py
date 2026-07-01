test = {
  'name': 'Lists',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [7//3, 5, [4, 0, 1], 2]
          >>> s[0]
          2
          >>> s[2]
          [4, 0, 1]
          >>> s[-1]
          2
          >>> len(s)
          4
          >>> 4 in s
          False
          >>> 4 in s[2]
          True
          >>> s[2] + [3 + 2]
          [4, 0, 1, 5]
          >>> 5 in s[2]
          False
          >>> s[2] * 2
          [4, 0, 1, 4, 0, 1]
          >>> list(range(3, 6))
          [3, 4, 5]
          >>> range(3, 6)
          92a2e1824db4e21d25feb5639b0fb925
          # locked
          >>> r = range(3, 6)
          >>> [r[0], r[2]]
          a7015b3a9656bcdd8e23b1956be648eb
          # locked
          >>> range(4)[-1]
          c66c489c94f153ccc42909baf6da3202
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
