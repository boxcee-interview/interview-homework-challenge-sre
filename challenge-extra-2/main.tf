locals {
  prefix         = "${path.module}/${var.manifests_folder}"
  manifest_paths = fileset(local.prefix, "**/*.yml")
  manifests_raw  = [for data in flatten([for path in local.manifest_paths : split("---", file("${local.prefix}/${path}"))]) : data]
  manifests_decoded = {for k, v in local.manifests_raw: "${lower(yamldecode(v).kind)}/${yamldecode(v).metadata.name}" => yamldecode(v)}
  namespaces = {for k, v in local.manifests_decoded: k => v if substr(k, 0, length("namespace")) == "namespace" }
  other_manifests = {for k, v in local.manifests_decoded: k => v if substr(k, 0, length("namespace")) != "namespace" }
}

resource "kubernetes_manifest" "namespaces" {
  for_each = local.namespaces
  manifest = each.value
}

resource "kubernetes_manifest" "other_manifests" {
  for_each = local.other_manifests
  manifest = each.value
  depends_on = [kubernetes_manifest.namespaces]
}