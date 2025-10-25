from setuptools import setup

setup(name='unifi-hotspot-logger',
      version='0.1',
      description='Simple webhook service that can log data coming from the unifi-hotspot app.',
      url='https://github.com/Thowaah/unifi-hotspot-logger',
      author='Thomas Weissgerber',
      author_email='thomas.weissgerber97@gmail.com',
      install_requires=[
          'flask',
          'markupsafe',
      ],
      zip_safe=False)
