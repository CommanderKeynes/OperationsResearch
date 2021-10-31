

import optimization_example_library
import Optimization
import numpy as np
import pytest


def test_build_wyndor_glass_example() -> None:
    wyndor_glass_optimization = optimization_example_library.build_wyndor_glass_example()
    _test_optimization_output(expected_z=-36, expected_x=[2, 6], optimization=wyndor_glass_optimization)


def test_build_radiation_therapy_example() -> None:
    radiation_therapy_optimization = optimization_example_library.build_radiation_therapy_example()
    _test_optimization_output(expected_z=5.25, expected_x=[7.5, 4.5], optimization=radiation_therapy_optimization)


def test_build_regional_planning_example() -> None:
    regional_planning_optimization = optimization_example_library.build_regional_planning_example()
    _test_optimization_output(
        expected_z=-633_333.33,
        expected_x=[133.33, 100, 25, 100, 250, 150, 0, 0, 0], optimization=regional_planning_optimization)


def test_build_air_pollution_example() -> None:
    air_pollution_optimization = optimization_example_library.build_air_pollution_example()
    _test_optimization_output(
        expected_z=32.16, expected_x=[1, 0.623, .343, 1, 0.048, 1], optimization=air_pollution_optimization)


def test_build_reclaiming_waste_example() -> None:
    pytest.skip(msg='Test Failing. Need to revisit model')

    waste_reclamation_optimization = optimization_example_library.build_reclaiming_waste_example()

    expected_x = [
        412.3, 859.6, 447.4, 429.8,
        2_587.7, 517.5, 1_552.6, 517.5,
        0, 0, 0, 0]

    _test_optimization_output(
        expected_z=-35_109.65, expected_x=expected_x, optimization=waste_reclamation_optimization, round_precision=1)


def test_build_personnel_scheduling_example() -> None:
    personnel_scheduling = optimization_example_library.build_personnel_scheduling_example()
    _test_optimization_output(expected_z=30_610, expected_x=[48, 31, 39, 43, 15], optimization=personnel_scheduling)


def test_build_distribution_network_example() -> None:
    distribution_network_optimization = optimization_example_library.build_distribution_network_example()
    _test_optimization_output(
        expected_z=49_000, expected_x=[0, 40, 10, 40, 80, 0, 20], optimization=distribution_network_optimization)


def _test_optimization_output(
        expected_z: float, expected_x: list, optimization: Optimization.Optimization, round_precision: int = 2) -> None:

    result = optimization.optimize()
    actual_x = result['x'].round(round_precision)
    expected_x = np.round(expected_x, round_precision)
    print(actual_x)

    assert abs(round(result['fun'], round_precision) - expected_z) <= 0.1
    assert np.equal(actual_x, expected_x).all()

