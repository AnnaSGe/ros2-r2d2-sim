import os
from glob import glob
from setuptools import setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='annas',
    maintainer_email='annas@todo.todo',
    description='ROS2 Python package',
    license='TODO',
    tests_require=['pytest'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
    ],
    entry_points={
        'console_scripts': [
            'talker = my_package.talker:main',
            'listener = my_package.listener:main',
        ],
        'console_scripts': [
            'move_robot = my_package.move_robot:main',
        ],
    },
)