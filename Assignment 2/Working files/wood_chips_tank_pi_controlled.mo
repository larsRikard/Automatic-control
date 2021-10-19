model wood_chips_tank_pi_controlled
  Modelica.Blocks.Continuous.Integrator h(y_start = 5)  annotation(
    Placement(visible = true, transformation(origin = {140, -76}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Division division annotation(
    Placement(visible = true, transformation(origin = {98, -74}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant rho(k = 145)  annotation(
    Placement(visible = true, transformation(origin = {-2, -54}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant A(k = 13.4)  annotation(
    Placement(visible = true, transformation(origin = {-2, -88}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Constant K_s(k = 0.5)  annotation(
    Placement(visible = true, transformation(origin = {2, 54}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Product product annotation(
    Placement(visible = true, transformation(origin = {52, -72}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Add sum_flow(k1 = -1)  annotation(
    Placement(visible = true, transformation(origin = {114, 10}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Step w_out(height = 33.33, offset = 25, startTime = 5000)  annotation(
    Placement(visible = true, transformation(origin = {84, 58}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Product w_in annotation(
    Placement(visible = true, transformation(origin = {60, 4}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Add error(k2 = -1)  annotation(
    Placement(visible = true, transformation(origin = {-120, 36}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Continuous.PI pi(T = 833.33, k = 10.935)  annotation(
    Placement(visible = true, transformation(origin = {-62, 36}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Step setpoint(height = 0, offset = 5, startTime = 0)  annotation(
    Placement(visible = true, transformation(origin = {-176, 48}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Nonlinear.FixedDelay tau(delayTime = 250) annotation(
    Placement(visible = true, transformation(origin = {-6, -6}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(division.y, h.u) annotation(
    Line(points = {{109, -74}, {116.5, -74}, {116.5, -76}, {128, -76}}, color = {0, 0, 127}));
  connect(rho.y, product.u1) annotation(
    Line(points = {{9, -54}, {39, -54}, {39, -66}}, color = {0, 0, 127}));
  connect(A.y, product.u2) annotation(
    Line(points = {{9, -88}, {39, -88}, {39, -78}}, color = {0, 0, 127}));
  connect(product.y, division.u2) annotation(
    Line(points = {{63, -72}, {75, -72}, {75, -80}, {86, -80}}, color = {0, 0, 127}));
  connect(sum_flow.y, division.u1) annotation(
    Line(points = {{125, 10}, {156.5, 10}, {156.5, -4}, {156, -4}, {156, -18}, {86, -18}, {86, -68}}, color = {0, 0, 127}));
  connect(w_out.y, sum_flow.u1) annotation(
    Line(points = {{95, 58}, {102, 58}, {102, 16}}, color = {0, 0, 127}));
  connect(K_s.y, w_in.u1) annotation(
    Line(points = {{13, 54}, {48, 54}, {48, 10}}, color = {0, 0, 127}));
  connect(w_in.y, sum_flow.u2) annotation(
    Line(points = {{71, 4}, {102, 4}}, color = {0, 0, 127}));
  connect(h.y, error.u2) annotation(
    Line(points = {{152, -76}, {170, -76}, {170, -110}, {-146, -110}, {-146, 30}, {-132, 30}}, color = {0, 0, 127}));
  connect(error.y, pi.u) annotation(
    Line(points = {{-108, 36}, {-74, 36}}, color = {0, 0, 127}));
  connect(setpoint.y, error.u1) annotation(
    Line(points = {{-164, 48}, {-148, 48}, {-148, 42}, {-132, 42}}, color = {0, 0, 127}));
  connect(pi.y, tau.u) annotation(
    Line(points = {{-51, 36}, {-36, 36}, {-36, -6}, {-18, -6}}, color = {0, 0, 127}));
  connect(tau.y, w_in.u2) annotation(
    Line(points = {{5, -6}, {27.5, -6}, {27.5, -2}, {48, -2}}, color = {0, 0, 127}));
  annotation(
    uses(Modelica(version = "4.0.0")),
  Diagram(coordinateSystem(extent = {{-200, -200}, {200, 200}})),
  Icon(coordinateSystem(extent = {{-200, -200}, {200, 200}})),
  version = "");
end wood_chips_tank_pi_controlled;
