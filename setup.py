from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows',
  'Operating System :: Unix',
  'Operating System :: MacOS',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='TeraTTS',
  version='1.0',
  description='russian text to speech',
  classifiers=classifiers,
  keywords='tts', 
  packages=find_packages(),
  install_requires=['scipy', 'sounddevice', 'onnxruntime', "tok", "transformers", "numpy", "sentencepiece", "ruaccent", "transliterate", "num2words"] 
)